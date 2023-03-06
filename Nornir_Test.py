from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)


results = nr.run(
    task=napalm_get, getters=["facts"]
)


print_result(results)