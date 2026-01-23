# Setup the ontokit. Do only once.
# Note that currently it is necessary to change 
# EMMOntoPy branch in github workflows to flb/issue916
#ontokit setup \
#  --ontology-name atomistic \
#  --ontology-prefix at \
#  --ontology-iri https://w3id.org/emmo/domain/atomistic \
#  . 

mkdir build
cp README.md LICENSE build/.

ontoconvert \
            -saw \
            --namespace="emmo:https://w3id.org/emmo#" \
            --namespace="at:https://w3id.org/emmo/domain/atomistic#" \
            atomistic-dependencies.ttl \
            build/atomistic-dependencies.ttl

ontoconvert \
            -sawe \
            --namespace="emmo:https://w3id.org/emmo#" \
            --namespace="at:https://w3id.org/emmo/domain/atomistic#" \
            --base-iri="https://w3id.org/emmo/domain/atomistic#" \
            --iri="https://w3id.org/emmo/domain/atomistic" \
            atomistic.ttl \
            build/atomistic.ttl

ontoconvert \
            -awe \
            --namespace="emmo:https://w3id.org/emmo#" \
            --namespace="at:https://w3id.org/emmo/domain/atomistic#" \
            --base-iri="https://w3id.org/emmo/domain/atomistic#" \
	    --iri="https://w3id.org/emmo/domain/atomistic" \
            --copy-annotation="elucidation-->http://purl.org/dc/terms/description" \
            --copy-annotation="prefLabel-->http://www.w3.org/2000/01/rdf-schema#label" \
            atomistic.ttl \
            build/atomistic-doc.ttl

robot reason \
            --reasoner HermiT \
            --remove-redundant-subclass-axioms true \
            --preserve-annotated-axioms true \
            --exclude-owl-thing true \
            --exclude-duplicate-axioms true \
            --input build/atomistic.ttl \
            --output atomistic-inferred.ttl

ontoconvert --iri=https://w3id.org/emmo/domain/atomistic/inferred atomistic-inferred.ttl build/atomistic-inferred.ttl
