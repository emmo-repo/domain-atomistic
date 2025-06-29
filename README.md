[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15767861.svg)](https://doi.org/10.5281/zenodo.15767861)
[![CI tests](https://github.com/emmo-repo/domain-atomistic/workflows/CI%20tests/badge.svg)](https://github.com/emmo-repo/domain-atomistic/actions/)
[![FOOPS Score](https://img.shields.io/badge/FOOPS%20Score-79.0%25-yellow)](https://foops.linkeddata.es/FAIR_validator.html)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)


Domain ontology for atomistic and electronic modelling
======================================================
An EMMO-based domain ontology for atomistic and electronic modelling.
![image](https://user-images.githubusercontent.com/45469701/145525645-4085c0de-efae-4975-811c-50730bde5ae2.png) <--- generated using https://www.ldf.fi/service/rdf-grapher --->

Status
------
- [ ] Proposal
- [X] accepted, under development
- [ ] official

This domain ontology is work-in-progress (WIP), it is in the process of being accepted as a task group by the EMMC.

* Application submitted: 15 June 2020
* Application accepted on: TBD


### Imported ontologies
Version dependencies on imported ontologies:

| Version | [EMMO]       | [crystallography] | [mechanics] |
|---------|--------------|-------------------|-------------|
| 0.0.1   | 1.0.0-alpha1 | 0.0.1             | 0.0.1       |
| 0.0.2   | 1.0.1        | 0.0.1             | 0.0.1       |
| 0.0.3   | 1.0.1        | 0.0.1             | 0.0.1       |



Obtaining domain-atomistic
--------------------------
This repository include the correct version of the crystallography and
mechanics domain ontologies as a git submodules.  Hence, use the
following command when cloning this repository:

    git clone --recurse-submodules --shallow-submodules git@github.com:emmo-repo/domain-atomistic.git


Attributions and credits
------------------------
### Authors
- Jesper Friis, SINTEF
- Francesca Lønstad Bleken, SINTEF
- Joana Francisco Morgado, Fraunhofer IWM
- Casper Welzel Andersen, EPFL

### Projects
- [MarketPlace](https://www.the-marketplace-project.eu/);
  Grant Agreement No: 760173
  <img src="https://www.the-marketplace-project.eu/content/dam/iwm/the-marketplace-project/images/MARKETPLACE_LOGO_300dpi.png" width="120">


License
-------
The atomistic domain ontology is released under the [Creative
Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode) license (CC BY 4.0).


[EMMO]: https://github.com/emmo-repo/EMMO
[CRYST]: https://github.com/emmo-repo/domain-crystallography
[MECH]: https://github.com/emmo-repo/domain-atomistic/mechanics.owl
