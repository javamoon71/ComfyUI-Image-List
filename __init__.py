# ComfyUI에 Image List 노드를 등록하는 진입점
from .nodes import ImageList

NODE_CLASS_MAPPINGS = {"ImageList": ImageList}
NODE_DISPLAY_NAME_MAPPINGS = {"ImageList": "Image List"}

WEB_DIRECTORY = "./web"
