#!/usr/bin/env python
"""Python script that generates the periodic table ontology.
"""
import warnings

import rdflib
from rdflib import URIRef, Literal
from rdflib.namespace import RDFS, OWL, DCTERMS

from emmo import World
import owlready2


__version__ = "0.0.1"  # Version of this ontology


def en(s):
    """Returns `s` as an English location string."""
    return owlready2.locstr(s, lang='en')


def pl(s):
    """Returns `s` as a plain literal string."""
    return owlready2.locstr(s, lang='')


# Check rdflib version (for preferred turtle serialising)
if not int(rdflib.__version__.split('.')[0]) >= 5:
    warnings.warn('upgrade to rdflib v5.0.0 or higher to get preferred output')

# Load crystallography, which imports emmo
crystallography_url = ('https://raw.githubusercontent.com/emmo-repo/'
                       'domain-crystallography/master/crystallography.ttl')
world = World()
cryst = world.get_ontology(crystallography_url)
cryst.load()
cryst.sync_python_names()  # Syncronize annotations

# Create new ontology
onto = world.get_ontology('http://emmo.info/atomistic#')
onto.base_iri = 'http://emmo.info/atomistic#'
onto.imported_ontologies.append(cryst)
onto.sync_python_names()


# Populate the new ontology
with onto:

    class ChargeDensity(onto.ISQDerivedQuantity):
        """Electric charge per volume."""
        physicalDimension = pl("T+1 L-3 M0 I+1 Θ0 N0 J0")

    class ChargeDensityDimension(onto.PhysicalDimension):
        equivalent_to = [onto.hasSymbolData.value(
            pl("T+1 L-3 M0 I+1 Θ0 N0 J0"))]



# Save new ontology as owl
onto.sync_attributes(name_policy='uuid', class_docstring='elucidation',
                     name_prefix='atomistic_')
onto.set_version(
    version_iri="http://emmo.info/%s/atomistic" % __version__)
onto.dir_label = False
onto.save('atomistic.owl', overwrite=True)


#################################################################
# Annotate the ontology itself with rdflib
#################################################################
BASE = rdflib.Namespace('http://emmo.info/atomistic')

g = rdflib.Graph()
g.parse('atomistic.owl', format='xml')

# Fix url to imported ontologies
for s, p, o in g.triples((None, OWL.imports, None)):
    if str(o) == 'http://emmo.info/crystallography/crystallography':
        g.remove((s, p, o))
        g.add((s, p, URIRef(crystallography_url)))

# Add ontology annotations
g.add((URIRef(BASE), OWL.versionInfo, Literal(__version__)))
g.add((URIRef(BASE), DCTERMS.title, Literal('Atomistic', lang='en')))
g.add((URIRef(BASE), DCTERMS.creator, Literal('Jesper Friis')))
g.add((URIRef(BASE), DCTERMS.contributor, Literal('SINTEF')))
g.add((URIRef(BASE), DCTERMS.creator, Literal('Francesca L. Bleken')))
g.add((URIRef(BASE), DCTERMS.contributor, Literal('SINTEF')))
g.add((URIRef(BASE), DCTERMS.publisher, Literal('EMMC ASBL')))
g.add((URIRef(BASE), DCTERMS.license,
       Literal('https://creativecommons.org/licenses/by/4.0/legalcode')))

g.add((URIRef(BASE), DCTERMS.abstract,
       Literal("""\
An EMMO-based domain ontology for atomistic and electronic modelling.

Atomistic is released under the Creative Commons Attribution 4.0 \
International license (CC BY 4.0).
""", lang='en')))

g.add((URIRef(BASE), RDFS.comment,
       Literal("""\
The EMMO requires FacT++ reasoner plugin in order to visualize all \
inferences and class hierarchy (ctrl+R hotkey in Protege).
""", lang='en')))


g.add((URIRef(BASE), RDFS.comment,
       Literal("""\
Contacts:
Jesper Friis
SINTEF
email: jesper.friis@sintef.no

Francesca L. Bleken
SINTEF
email: francesca.l.bleken@sintef.no
""", lang='en')))

# Store in turtle format
g.serialize(destination='atomistic.ttl', format='turtle', base=BASE)
