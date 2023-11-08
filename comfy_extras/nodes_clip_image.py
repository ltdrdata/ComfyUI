

class CLIPImageConditioning:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"clip_vision_output": ("CLIP_VISION_OUTPUT", ),
                             }}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "image_cond"

    CATEGORY = "advanced/conditioning"

    def image_cond(self, clip_vision_output):
        return ([[clip_vision_output.last_hidden_state, {}]], )



NODE_CLASS_MAPPINGS = {
    "CLIPImageConditioning": CLIPImageConditioning,
}
