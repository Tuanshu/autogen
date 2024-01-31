#%%
import autogen
from autogen.code_utils import implement
config_list_deepseek = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["deepseek-coder-6.7b-instruct"],
    },
)
config_list_openchat = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["openchat_3.5"],
    },
)

print(type(config_list_deepseek))
#%%
definition="""class Interface:
    def add(self, num1,num2):
        return NotImplementedError"""

configs=config_list_deepseek
implement(definition,configs)