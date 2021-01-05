#!/usr/bin/env python
"""Python script that generates the periodic table ontology.
"""
import os
import subprocess
import warnings

import ase

import rdflib
from rdflib import URIRef, Literal, SKOS
from rdflib.namespace import RDFS, OWL, DCTERMS

from emmo import World, get_ontology

__version__ = "0.0.1"

thisdir = os.path.abspath(os.path.dirname(__file__))


# Check rdflib version (for preferred turtle serialising)
if not int(rdflib.__version__.split('.')[0]) >= 5:
    warnings.warn('upgrade to rdflib v5.0.0 or higher to get preferred output')

# Load crystallography, which imports emmo
world = World()
cryst = world.get_ontology('https://raw.githubusercontent.com/emmo-repo/domain-crystallography/master/crystallography.ttl')
cryst.load()
cryst.sync_python_names() #Syncronize annotations

# Create new ontology
onto = world.get_ontology('http://emmo.info/atomistic#')
onto.base_iri = 'http://emmo.info/atomistic#'
onto.imported_ontologies.append(cryst)
onto.sync_python_names()


# Populate the new ontology
with onto:

    class ChargeDensity(onto.ISQDerivedQuantity):
        """Electric charge per volume"""
        elucidation = "Electric charge per volume"
        physicalDimension = "T+1 L-3 M0 I+1 Θ0 N0 J0"


    class ChargeDensityDimension(onto.PhysicalDimension):
        """ """
        equivalent_to = [onto.hasSymbolData.value("T+1 L-3 M0 I+1 Θ0 N0 J0")]



# Save new ontology as owl
onto.sync_attributes(name_policy='uuid', name_prefix='atomistic_')
onto.set_version(
    version_iri="http://emmo.info/atomistic/0.0.1")
onto.dir_label = False
onto.save(os.path.join(thisdir, 'atomistic.owl'), overwrite=True)


# Do final manipulation with rdflib
BASE = rdflib.Namespace('http://emmo.info/atomistic')

g = rdflib.Graph()
#g.bind('skos', rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#'))
g.bind('', rdflib.term.URIRef('http://emmo.info/atomistic#'))
g.parse('atomistic.owl', format='xml')

# Add version to imported ontologies
crystallographyversion = '0.0.1'
#for s, p, o in g.triples((None, OWL.imports, None)):
#    o2 = URIRef(o.replace('http://emmo.info/emmo/',
#                          'http://emmo.info/emmo/%s/' % emmoversion))
#
#    g.remove((s, p, o))
#    g.add((s, p, o2))

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
       Literal('''\
An EMMO-based domain ontology for atomistic and electronic modelling.

Atomistic is released under the Creative Commons Attribution 4.0 \
International license (CC BY 4.0).
''', lang='en')))

g.add((URIRef(BASE), RDFS.comment,
       Literal('''\
The EMMO requires FacT++ reasoner plugin in order to visualize all \
inferences and class hierarchy (ctrl+R hotkey in Protege).
''', lang='en')))


g.add((URIRef(BASE), RDFS.comment,
       Literal('''\
Contacts:
Jesper Friis
SINTEF
email: jesper.friis@sintef.no

Francesca L. Bleken
SINTEF
email: francesca.l.bleken@sintef.no
''', lang='en')))

# Store in turtle format
g.serialize(destination='atomistic.ttl', format='turtle', base=BASE)
