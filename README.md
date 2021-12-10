[![CI tests](https://github.com/emmo-repo/domain-atomistic/workflows/CI%20tests/badge.svg)](https://github.com/emmo-repo/domain-atomistic/actions/)


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


Imported ontologies
-------------------
This ontology builds on top of EMMO. See the following table for version
compatibilies:

| Imported Ontologies  | Version           |
| -------------------- | ----------------- |
| [EMMO][1]            | 1.0.0-alpha2      |
| [crystallography][2] | 0.0.1             |
| [mechanics][3]       | 0.0.1             |


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


[1]: https://github.com/emmo-repo/EMMO
[2]: https://github.com/emmo-repo/domain-crystallography
[3]: https://github.com/emmo-repo/domain-atomistic/mechanics.owl
