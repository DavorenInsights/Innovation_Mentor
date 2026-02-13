# app_config.py
import os
MODE = os.getenv("IM_MODE", "public")  # "public" or "institutional"
PUBLIC = MODE == "public"
