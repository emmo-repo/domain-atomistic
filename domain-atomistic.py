#!/usr/bin/env python
"""Python script that generates the periodic table ontology.
"""

from emmo import World
from emmo.utils import write_catalog
import owlready2


__version__ = "0.0.1"  # Version of this ontology


def en(s):
    """Returns `s` as an English location string."""
    return owlready2.locstr(s, lang='en')


def pl(s):
    """Returns `s` as a plain literal string."""
    return owlready2.locstr(s, lang='')


# Load crystallography, which imports emmo
emmo_url = (
        'https://raw.githubusercontent.com/emmo-repo/emmo-repo.github.io/'
        'master/versions/1.0.0-beta/emmo-inferred-chemistry2.ttl')
world = World()
emmo = world.get_ontology(emmo_url)
emmo.load()
emmo.sync_python_names()  # Syncronize annotations
emmo.base_iri = emmo.base_iri.rstrip('/#')
catalog_mappings = {emmo.base_iri: emmo_url}

# Create new ontology
onto = world.get_ontology('http://emmo.info/domain-atomistic#')
onto.imported_ontologies.append(emmo)
onto.sync_python_names()


# Populate the new ontology
with onto:

    #
    # ObjectProperties
    # ----------------
    class hasEigenvalue(onto.hasProperty):
        """Relates a mathematical (or physical) operator to its eigenvalue."""
        domain = [onto.MathematicalOperator]

    #
    # Classes
    # -------
    class ChargeDensity(onto.ISQDerivedQuantity):
        """Electric charge per volume."""
        physicalDimension = pl("T+1 L-3 M0 I+1 Θ0 N0 J0")
        IECEntry = pl("http://www.electropedia.org/iev/iev.nsf/display?"
                      "openform&ievref=121-11-07")
        iupacEntry = pl("https://doi.org/10.1351/goldbook.C00988")
        omMatch = pl("http://www.ontology-of-units-of-measure.org/resource/"
                     "om-2/ElectricChargeDensity")
        wikipediaEntry = "https://en.wikipedia.org/wiki/Charge_density"

    class ChargeDensityDimension(onto.PhysicalDimension):
        """Physical dimensionality of charge density."""
        equivalent_to = [onto.hasSymbolData.value(
            pl("T+1 L-3 M0 I+1 Θ0 N0 J0"))]

    class DensityFunctionalTheory(onto.ElectronicModel):
        """An efficient computional method for solving the many-electron
        (time-independent) Schrödinger equation."""

    class PhysicalOperator(onto.MathematicalOperator):
        """A mathematical operator with a physical interpretation."""

    class Hamiltonian(onto.PhysicalOperator):
        """An operator corresponding to the sum of the kinetic energies plus
        the potential energies for all the particles in the system."""
        is_a = [onto.Object, onto.hasEigenvalue.some(onto.Energy)]

    class WaveFunction(onto.ISQDimensionlessQuantity):
        """A mathematical description of the quantum state of an isolated
        quantum system. A wave function is a function of the degrees
        of freedom corresponding to some maximal set of commuting
        observables. Once such a representation is chosen, the wave
        function can be derived from the quantum state.
        """
        physicalDimension = pl("T0 L0 M0 I0 Θ0 N0 J0")
        wikipediaEntry = pl("https://en.wikipedia.org/wiki/Wave_function")

    class SchrodingerEquation(onto.PhysicsEquation):
        """A linear partial differential equation describing the wave
        function of a quantum-mechanical system.

        The exact form of the Schrödinger equation depends on the
        physical situation.  The most general form is the
        time-dependent Schrödinger equation.
        """
        altLabel = en("SchrödingerEquation")
        is_a = [onto.hasSpatialDirectPart.some(onto.Energy),
                onto.hasSpatialDirectPart.some(onto.Hamiltonian),
                onto.hasSpatialDirectPart.some(onto.WaveFunction)]
        wikipediaEntry = pl(
            "https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation")

    class TimeDependentSchrodingerEquation(onto.SchrodingerEquation):
        """The full time-dependent Schrödinger equation."""
        altLabel = en("TimeDependentSchrödingerEquation")

    class TimeIndependentSchrodingerEquation(onto.SchrodingerEquation):
        """If the external potential does not depende on time, the Schrödinger
        equation can be reduced to this time-independent form.
        """
        altLabel = en("TimeIndependentSchrödingerEquation")

    class KohnShamEquation(onto.TimeIndependentSchrodingerEquation):
        """The Schrödinger equation for a fictious "Kohn-Sham" system of
        non-interacting electrons that generates the same charge
        density as the real interacting system.
        """
        comment = ("This is the equation that is solved with density "
                   "functional theory.")
        is_a = [onto.hasSpatialDirectPart.some(onto.ChargeDensity)]


# Save new ontology as owl
onto.sync_attributes(name_policy='uuid', class_docstring='elucidation',
                     name_prefix='')
version_iri = "http://emmo.info/%s/domain-atomistic" % __version__
onto.set_version(version_iri=version_iri)
onto.dir_label = False

catalog_mappings[version_iri] = 'atomistic.ttl'

#################################################################
# Annotate the ontology metadata
#################################################################

onto.metadata.abstract.append(en(
        'An EMMO-based domain ontology for atomistic and electronic modelling.'
        'Atomistic is released under the Creative Commons Attribution 4.0 '
        'International license (CC BY 4.0).'))

onto.metadata.title.append(en('Atomistic'))
onto.metadata.creator.append(en('Jesper Friis'))
onto.metadata.contributor.append(en('SINTEF'))
onto.metadata.creator.append(en('Francesca L. Bleken'))
onto.metadata.contributor.append(en('SINTEF'))
onto.metadata.publisher.append(en('EMMC ASBL'))
onto.metadata.license.append(en(
    'https://creativecommons.org/licenses/by/4.0/legalcode'))
onto.metadata.versionInfo.append(en(__version__))
onto.metadata.comment.append(en(
    'The EMMO requires FaCT++ reasoner plugin in order to visualize all'
    'inferences and class hierarchy (ctrl+R hotkey in Protege).'))
onto.metadata.comment.append(en(
    'This ontology is generated with data from the ASE Python package.'))
onto.metadata.comment.append(en(
    'Contacts:\n'
    'Jesper Friis\n'
    'SINTEF\n'
    'email: jesper.friis@sintef.no\n'
    '\n'
    'Francesca L. Bleken\n'
    'SINTEF\n'
    'email: francesca.l.bleken@sintef.no'
    ))


onto.save('atomistic.ttl', overwrite=True)
write_catalog(catalog_mappings)
# onto.sync_reasoner()
# onto.save('atomistic-inferred.ttl', overwrite=True)


# Manually change url of EMMO to `emmo_url` when importing it to make
# it resolvable without consulting the catalog file.  This makes it possible
# to open the ontology from url in Protege
import rdflib  # noqa: E402, F401
g = rdflib.Graph()
g.parse('atomistic.ttl', format='turtle')
for s, p, o in g.triples(
        (None, rdflib.URIRef('http://www.w3.org/2002/07/owl#imports'), None)):
    if 'emmo-inferred' in o:
        g.remove((s, p, o))
        g.add((s, p, rdflib.URIRef(emmo_url)))
g.serialize(destination='atomistic.ttl', format='turtle')
