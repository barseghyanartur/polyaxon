
To access information about a Polyaxon run:

```python
from polyaxon_client.tracking import (
    get_outputs_path,
    get_outputs_refs_paths,
    get_data_paths,
    get_log_level
)
``` 


 * `get_outputs_path`: The outputs path generated by polyaxon based on the hierarchy of the experiment.

        `user/project/group/experiment/files`

 * `get_outputs_refs_paths`: The references outputs paths requested by the user,
    the order follows the order specified by the user:

        {
            'jobs': [
                `user/project/job12/files`,
            ], 'experiments': [
                `user/project/group/experiment1/files`,
                `user/project/experiment100/files`
            ]
        }

 * `get_data_paths`: The data paths mounted for the job/experiment:

        {
          'data1': '/data/1',
          'data-foo': '/data/foo',
        }

 * `get_log_level`: If set on the polyaxonfile it will return the log level.

