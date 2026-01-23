# Setup the ontokit. Do only once.
# Note that currently it is necessary to change 
# EMMOntoPy branch in github workflows to flb/issue916
#ontokit setup \
#  --ontology-name atomistic \
#  --ontology-prefix at \
#  --ontology-iri https://w3id.org/emmo/domain/atomistic \
#  . 

#mkdir build

#ontoconvert \
#      -awe \
#      --namespace="emmo:https://w3id.org/emmo#" \
#      --namespace="at:https://w3id.org/emmo/domain/atomistic#" \
#      --base-iri="https://w3id.org/emmo/domain/atomistic#" \
#      --iri="https://w3id.org/emmo/domain/atomistic" \
#      --copy-annotation="elucidation-->http://purl.org/dc/terms/description" \
#      --copy-annotation="prefLabel-->http://www.w3.org/2000/01/rdf-schema#label" \
#      atomistic.ttl \
#      build/atomistic-doc.ttl

#keywords -i build/atomistic-doc.ttl --keywords build/atomistic.md --namespace-filter=https://w3id.org/emmo/domain/atomistic --redefine=allow #-p ato=https://w3id.org/emmo/domain/atomistic
