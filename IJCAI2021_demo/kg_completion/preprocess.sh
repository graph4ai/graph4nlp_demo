#!/bin/bash
mkdir kg_completion/data
mkdir kg_completion/data/kinship
mkdir kg_completion/saved_models
tar -xvf kg_completion/kinship/raw/kinship.tar.gz -C kg_completion/data/kinship
python kg_completion/wrangle_KG.py kinship
