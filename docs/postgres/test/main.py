from os.path import abspath, dirname
import sys

sys.path.insert(0, dirname(abspath(__file__)))

from entities import create_entities
from add_clients_into_table import insert_example_clients
from search_all_clients_into_table import  show_all_clients

create_entities()
insert_example_clients()
show_all_clients()