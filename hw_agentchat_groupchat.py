#%%
import autogen

#%%
# config_list_gpt4 = autogen.config_list_from_json(
#     "OAI_CONFIG_LIST",
#     filter_dict={
#         "model": ["gpt-4", "gpt-4-0314", "gpt4", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
#     },
# )

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


# config_list_gpt35 = autogen.config_list_from_json(
#     "OAI_CONFIG_LIST",
#     filter_dict={
#         "model": {
#             "gpt-3.5-turbo",
#             "gpt-3.5-turbo-16k",
#             "gpt-3.5-turbo-0301",
#             "chatgpt-35-turbo-0301",
#             "gpt-35-turbo-v0301",
#         },
#     },
# )

#%%
llm_config_deepseek = {"config_list": config_list_deepseek, "cache_seed": 42}
llm_config_openchat = {"config_list": config_list_openchat, "cache_seed": 42}


user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={
        "last_n_messages": 2, 
        "work_dir": "groupchat",
        "use_docker": True,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    #code_execution_config=False,  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    human_input_mode="TERMINATE",
)
coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config_deepseek,
)
pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Creative in software product ideas.",
    llm_config=llm_config_openchat,
)
groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config_openchat)

#%%
test_message1="please create a project with two folder, 'domain' and 'infrastructure'. then, create a interface.py in `domain` folder, then create a impl.py in 'infrastructure'. the method I need is `add` to add two numerical number."
test_message2="please write a helloworld.py that can be used to sum two numerical numbers."

user_proxy.initiate_chat(
    manager, message=test_message2
)
# type exit to terminate the chat
# %%
