from typing import Any, Dict
from django.views.generic import TemplateView


class MainMixins(TemplateView):
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # write code
        # ...
        return context
