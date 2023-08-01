from aifs_client.paths.annotation_templates.get import ApiForget
from aifs_client.paths.annotation_templates.put import ApiForput
from aifs_client.paths.annotation_templates.post import ApiForpost


class AnnotationTemplates(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
