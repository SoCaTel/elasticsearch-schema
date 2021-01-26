<img src="https://platform.socatel.eu/images/socatel-logo.png" alt="SoCaTelLogo" width="250" />

### SoCaTel Elasticsearch indices

This repository provides with a convenience script that will create the required Elasticsearch indices to operate 
components within the SoCaTel repository. Install the necessary [requirements](./requirements.txt) and run the
 [script](./insert_indices.py) to create these with their corresponding schema that replicates that used for the
  SoCaTel platform.
  
#### Prerequisites

Setup an Elasticsearch instance of at least version 7.2.0. The choice of deployment lies with the developer, this can
 either be a containerised setup or hosted directly on a machine/server accessible through the network that SoCaTel
  components will be deployed. We provide a [docker compose file](docker_elastic_setup/docker-compose.yml) that you can use to setup
   Elasticsearch version 7.10.0 by executing:
   
   `docker-compose -f docker-compose.yml up -d` 

**NOTE** This repository has been developed using Python 3.6

## **Contact**
If you encounter any problems, please contact the following:

[<img src="https://www.cyric.eu/wp-content/uploads/2017/04/cyric_logo_2017.svg" alt="CyRIC | Cyprus Research and Innovation Centre" width="150" />](mailto:info@cyric.eu)

## License

All software components and schema definitions listed under this repository are licensed under:

[Apache-2.0](LICENSE)

## Acknowledgments

* [SoCaTel project](https://www.socatel.eu/)
* [Horizon 2020](https://ec.europa.eu/programmes/horizon2020/en)