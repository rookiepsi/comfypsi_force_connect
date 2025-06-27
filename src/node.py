from comfy.comfy_types.node_typing import IO


class ForceConnect:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "source": (IO.ANY,),
            }
        }

    RETURN_TYPES = (IO.ANY,)
    FUNCTION = "main"
    CATEGORY = "comfypsi/utility"

    def main(self, source):
        return (source,)


NODE_CLASS_MAPPINGS = {"comfypsi_force_connect": ForceConnect}
NODE_DISPLAY_NAME_MAPPINGS = {"comfypsi_force_connect": "Force Connect"}
