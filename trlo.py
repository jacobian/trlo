import configglue.glue
import configglue.parser
import configglue.schema
from unipath import FSPath as Path

class TrloSchema(configglue.schema.Schema):
    client_key = configglue.schema.StringOption(fatal=True)
    client_secret = configglue.schema.StringOption(fatal=True)
    owner_key = configglue.schema.StringOption()
    owner_secret = configglue.schema.StringOption()

parser = configglue.parser.SchemaConfigParser(TrloSchema())
parser.read([Path('~/.trlo').expand()])
op, opts, args = configglue.glue.schemaconfigglue(parser)
is_valid, reasons = parser.is_valid(report=True)
if not is_valid:
    op.error(reasons[0])

print opts
print args
