
:html_theme.sidebar_secondary.remove:

======================
Domain Atomistic Terms
======================

**Domain ontology for atomistic and electronic structure modelling.**


This page lists all terms extracted from the domain atomistic ontology. It is intended to serve as a reference resource. 


Atomistic
=========


----

.. raw:: html

   <div id="83a69cf2-00c1-58b8-915b-76cb3549890a"></div>

DensityFunctionalTheory
-----------------------

IRI: https://w3id.org/emmo/domain/atomistic#83a69cf2-00c1-58b8-915b-76cb3549890a

.. raw:: html

  <table class="element-table">
  <tr>
    <td class="element-table-key"><span class="element-table-key">Elucidation</span></td>
    <td class="element-table-value">An efficient computional method for solving the many-electron (time-independent) Schrödinger equation.</td>
  </tr>
  </table>


----

.. raw:: html

   <div id="42244404-98d1-582a-8fc0-3cdd2a9b3df6"></div>

Hamiltonian
-----------

IRI: https://w3id.org/emmo/domain/atomistic#42244404-98d1-582a-8fc0-3cdd2a9b3df6

.. raw:: html

  <table class="element-table">
  <tr>
    <td class="element-table-key"><span class="element-table-key">Elucidation</span></td>
    <td class="element-table-value">An operator corresponding to the sum of the kinetic energies plus the potential energies for all the particles in the system.</td>
  </tr>
  <tr>
    <td class="element-table-key"><span class="element-table-key">Parent Classes</span></td>
    <td class="element-table-value"><a href='#08fd7117-66ac-5b6d-b65e-34a826675877'>PhysicalOperator</a></td>
  </tr>
  </table>


----

.. raw:: html

   <div id="b65fe3b6-8477-5508-a066-2f7edcf25126"></div>

KohnShamEquation
----------------

IRI: https://w3id.org/emmo/domain/atomistic#b65fe3b6-8477-5508-a066-2f7edcf25126

.. raw:: html

  <table class="element-table">
  <tr>
    <td class="element-table-key"><span class="element-table-key">Elucidation</span></td>
    <td class="element-table-value">The Schrödinger equation for a fictious "Kohn-Sham" system of non-interacting electrons that generates the same charge density as the real interacting system.</td>
  </tr>
  <tr>
    <td class="element-table-key"><span class="element-table-key">Comment</span></td>
    <td class="element-table-value">This is the equation that is solved with density functional theory.</td>
  </tr>
  <tr>
    <td class="element-table-key"><span class="element-table-key">Parent Classes</span></td>
    <td class="element-table-value"><a href='#acaafcb6-b65f-5996-93ed-2f486f5f2b30'>TimeIndependentSchrodingerEquation</a></td>
  </tr>
  </table>


----

.. raw:: html

   <div id="08fd7117-66ac-5b6d-b65e-34a826675877"></div>

PhysicalOperator
----------------

IRI: https://w3id.org/emmo/domain/atomistic#08fd7117-66ac-5b6d-b65e-34a826675877

.. raw:: html

  <table class="element-table">
  <tr>
    <td class="element-table-key"><span class="element-table-key">Elucidation</span></td>
    <td class="element-table-value">A mathematical operator with a physical interpretation.</td>
  </tr>
  <tr>
    <td class="element-table-key"><span class="element-table-key">Subclasses</span></td>
    <td class="element-table-value"><a href='#42244404-98d1-582a-8fc0-3cdd2a9b3df6'>Hamiltonian</a></td>
  </tr>
  </table>


----

.. raw:: html

   <div id="c4dd4450-cc80-5de4-a8d6-db0651115a2c"></div>

SchrodingerEquation
-------------------

IRI: https://w3id.org/emmo/domain/atomistic#c4dd4450-cc80-5de4-a8d6-db0651115a2c

.. raw:: html

  <table class="element-table">
  <tr>
    <td class="element-table-key"><span class="element-table-key">Elucidation</span></td>
    <td class="element-table-value">A linear partial differential equation describing the wave function of a quantum-mechanical system. The exact form of the Schrödinger equation depends on the physical situation.  The most general form is the time-dependent Schrödinger equation.</td>
  </tr>
  <tr>
    <td class="element-table-key"><span class="element-table-key">Wikipedia Reference</span></td>
    <td class="element-table-value"><a href='https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation'>https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation</a></td>
  </tr>
  <tr>
    <td class="element-table-key"><span class="element-table-key">Subclasses</span></td>
    <td class="element-table-value"><a href='#acaafcb6-b65f-5996-93ed-2f486f5f2b30'>TimeIndependentSchrodingerEquation</a>, <a href='#fac61002-4a3d-5810-a430-ad5dad69c9a0'>TimeDependentSchrodingerEquation</a></td>
  </tr>
  </table>


----

.. raw:: html

   <div id="fac61002-4a3d-5810-a430-ad5dad69c9a0"></div>

TimeDependentSchrodingerEquation
--------------------------------

IRI: https://w3id.org/emmo/domain/atomistic#fac61002-4a3d-5810-a430-ad5dad69c9a0

.. raw:: html

  <table class="element-table">
  <tr>
    <td class="element-table-key"><span class="element-table-key">Elucidation</span></td>
    <td class="element-table-value">The full time-dependent Schrödinger equation.</td>
  </tr>
  <tr>
    <td class="element-table-key"><span class="element-table-key">Parent Classes</span></td>
    <td class="element-table-value"><a href='#c4dd4450-cc80-5de4-a8d6-db0651115a2c'>SchrodingerEquation</a></td>
  </tr>
  </table>


----

.. raw:: html

   <div id="acaafcb6-b65f-5996-93ed-2f486f5f2b30"></div>

TimeIndependentSchrodingerEquation
----------------------------------

IRI: https://w3id.org/emmo/domain/atomistic#acaafcb6-b65f-5996-93ed-2f486f5f2b30

.. raw:: html

  <table class="element-table">
  <tr>
    <td class="element-table-key"><span class="element-table-key">Elucidation</span></td>
    <td class="element-table-value">If the external potential does not depende on time, the Schrödinger equation can be reduced to this time-independent form.</td>
  </tr>
  <tr>
    <td class="element-table-key"><span class="element-table-key">Parent Classes</span></td>
    <td class="element-table-value"><a href='#c4dd4450-cc80-5de4-a8d6-db0651115a2c'>SchrodingerEquation</a></td>
  </tr>
  <tr>
    <td class="element-table-key"><span class="element-table-key">Subclasses</span></td>
    <td class="element-table-value"><a href='#b65fe3b6-8477-5508-a066-2f7edcf25126'>KohnShamEquation</a></td>
  </tr>
  </table>


----

.. raw:: html

   <div id="df750ce7-fda1-5e9b-ba32-db96ec170577"></div>

WaveFunction
------------

IRI: https://w3id.org/emmo/domain/atomistic#df750ce7-fda1-5e9b-ba32-db96ec170577

.. raw:: html

  <table class="element-table">
  <tr>
    <td class="element-table-key"><span class="element-table-key">Elucidation</span></td>
    <td class="element-table-value">A mathematical description of the quantum state of an isolated quantum system. A wave function is a function of the degrees of freedom corresponding to some maximal set of commuting observables. Once such a representation is chosen, the wave function can be derived from the quantum state.</td>
  </tr>
  <tr>
    <td class="element-table-key"><span class="element-table-key">Wikipedia Reference</span></td>
    <td class="element-table-value"><a href='https://en.wikipedia.org/wiki/Wave_function'>https://en.wikipedia.org/wiki/Wave_function</a></td>
  </tr>
  </table>


----

.. raw:: html

   <div id="42812fef-145a-56e9-9c18-72bd32214455"></div>

hasEigenvalue
-------------

IRI: https://w3id.org/emmo/domain/atomistic#42812fef-145a-56e9-9c18-72bd32214455

.. raw:: html

  <table class="element-table">
  <tr>
    <td class="element-table-key"><span class="element-table-key">Elucidation</span></td>
    <td class="element-table-value">Relates a mathematical (or physical) operator to its eigenvalue.</td>
  </tr>
  </table>

End of Document.
