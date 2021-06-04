import argparse

from graph4nlp.pytorch.modules.config import get_basic_args
from graph4nlp.pytorch.modules.utils.config_utils import update_values, get_yaml_config


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_yaml", type=str,
                        default="examples/pytorch/semantic_parsing/graph2seq/config/new_dependency_gat_bi_sep.yaml", help="")
                        # default="examples/pytorch/semantic_parsing/graph2seq/config/new_dynamic_refine.yaml", help="")
                        # default = "examples/pytorch/semantic_parsing/graph2seq/config/new_dynamic.yaml", help = "")

                        # default="examples/pytorch/semantic_parsing/graph2seq/config/new_constituency.yaml", help="")


    cfg = parser.parse_args()

    our_args = get_yaml_config(cfg.dataset_yaml)
    template = get_basic_args(graph_construction_name=our_args["graph_construction_name"],
                              graph_embedding_name=our_args["graph_embedding_name"],
                              decoder_name=our_args["decoder_name"])
    update_values(to_args=template, from_args_list=[our_args, our_args["other_args"]])
    return template
