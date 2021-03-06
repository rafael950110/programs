import Text.ParserCombinators.Parsec
import Text.ParserCombinators.Parsec.Expr
import Text.ParserCombinators.Parsec.Language
import qualified Text.ParserCombinators.Parsec.Token as P

data Expr = Natural Integer
          | Var String
          | Fun String Expr
          | App Expr Expr
  deriving (Show)

lexer :: P.TokenParser ()
lexer = P.makeTokenParser (haskellDef { reservedOpNames = ["*", "/", "+", "-"] })

natural     = P.natural lexer
parens      = P.parens lexer
reservedOp  = P.reservedOp lexer
identifier  = P.identifier lexer
lexeme      = P.lexeme lexer

expr :: Parser Expr
expr = buildExpressionParser table term <|> fun <?> "expression"
  where
    table = [[unary "-" "negate"],
             [binop "*" AssocLeft, binop "/" AssocLeft],
             [binop "+" AssocLeft, binop "-" AssocLeft]]
    binop op assoc = Infix (do{ reservedOp op; return $ \x y -> App (App (Var op) x) y } <?> "operator") assoc
    unary s op = Prefix (do{ reservedOp s; return $ App (Var op) })

term :: Parser Expr
term = try(app) <|> try(factor)

factor :: Parser Expr
factor = parens expr <|> (Natural <$> natural) <|> (Var <$> identifier) <?> "factor"

fun :: Parser Expr
fun = Fun <$> (lexeme (char '\\') *> identifier) <*> (lexeme (string "->") *> expr)

app :: Parser Expr
app = App <$> factor <*> factor

stmt :: Parser Expr
stmt = expr <* eof

main = do
  print $ parse stmt "" "(\\x -> x * x) 111"
  print $ parse stmt "" "(\\square -> square 111) (\\x -> x * x)"
  print $ parse stmt "" "\\f -> \\x -> f x + 1"