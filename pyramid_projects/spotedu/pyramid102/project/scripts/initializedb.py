import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    set_up_tables,
    )

from ..models.user import User
from ..models.task import Task


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    set_up_tables(engine)
    with transaction.manager:
        u1=User('jozko', 'jozko@mrkvicka.sk')
        u2=User('ferko', 'ferko@fetacisko.sk')
        t1=Task('zasad mrkvu', u1)
        t2=Task('nefetuj tolko', u2)
        DBSession.add_all([u1,u2,t1,t2])
