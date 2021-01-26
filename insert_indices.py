import yaml
import time

from urllib.parse import quote_plus as urlquote
from elasticsearch import Elasticsearch as EsClient
from elasticsearch.client import IndicesClient as IdxClient

if __name__ == "__main__":
    with open("config.yml", 'r') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)

    auth_str = ""
    if cfg['elasticsearch']['user'] is not None and cfg['elasticsearch']['passwd'] is not None:
        auth_str = cfg['elasticsearch']['user'] + ':' +\
                   urlquote(cfg['elasticsearch']['passwd']) + '@'

    es = EsClient(['http://' + auth_str +
                   cfg['elasticsearch']['host'] + ':' +
                   cfg['elasticsearch']['port']],
                  verify_certs=True)

    ic = IdxClient(es)

    for idx in cfg['indices']:
        if not ic.exists(index=idx):
            ic.create(index=idx, body=cfg['indices'][idx]["body"])
            # Give some time to have the index fully created
            time.sleep(1)
