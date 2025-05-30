# BiasAskerCustom

Install requirements.txt and:
pip install -U spacy
python -m spacy download en_core_web_lg


# BiasAsker: Measuring the Bias in Conversational AI System

This is the artifact for the paper ["***BiasAsker: Measuring the Bias in Conversational AI System***"](https://arxiv.org/abs/2305.12434). This artifact supplies the BiasAsker toolkit and supplementary materials for the paper. This repository contains:

1. Code implementation of BiasAsker, i.e., the Python script and instructions to run BiasAsker to test dialog models specified in the paper.
2. Complete dataset. The complete datasets are in `/dataset` and also on [Huggingface 🤗](https://huggingface.co/datasets/iforgott/BiasAsker). The sample of our annotated social groups and social biases dataset used in our experiment (with and without API) is in `/data`. 
3. Complete bias association visualization of all chatbots under test. In `/figs/all_results.zip`, we provide all the visualization results of chatbots under test, including group comparisons for absolute biases and bias association for relative biases.

**Quick Links**

[Abstract](#Abstract) | [Insights](#Insights) | [Dataset 🤗](https://huggingface.co/datasets/iforgott/BiasAsker) | [Code Usage](#Code) 



# Abstract

Powered by advanced Artificial Intelligence (AI) techniques, conversational AI systems, such as chatbots and digital assistants, have been widely deployed in daily life.  However, such systems may still produce content containing biases and stereotypes, causing potential social problems. In this paper, we propose BiasAsker, an automated framework to identify and measure social bias in conversational AI systems, and an auxiliary dataset containing 1,262 social groups and 7,343 biased properties. Given the dataset, BiasAsker automatically generates questions and  adopts a novel method based on existence measurement to identify two types of biases (absolute bias and related bias) in conversational systems. Extensive experiments on 8 commercial systems and 2 famous research models show that 32.83% of the questions generated by BiaAsker can trigger biased behaviors in these widely deployed conversational systems. 

![image-20250104232924587](./assets/pipeline.png)

# Insights

**DialoGPT favors men over all other groups. Jovi negatively associates transgender people with health, mistreatment, and morality, and men with morality.**

<img src="./assets/gender.png" alt="image-20250104232924587" style="zoom:30%;" />

**Jovi tends to choose young people over other people when queried with positive descriptions concerning social status, and DialoGPT exhibits similar behavior.**

<img src="./assets/social.png" alt="image-20250104232924587" style="zoom:30%;" />

**Transgender people and old people have the highest preference rate in ChatGPT. In general, groups receiving the most preference rate from ChatGPT are the groups that tend to receive consistently less preference from other conversational systems.**

<img src="./assets/chatgpt.png" alt="image-20250104232924587" style="zoom:30%;" />

# Code

## Environment Setup

Please install the required modules specified in `requirements.txt`.

## Testing Chatbots

To run a full experiment on a chatbot (i.e., generate questions, collect answers, evaluate answers, plot visualizations, export statistics), use `python experiment.py full <bot name>`, where \<bot name\> can be one of the following: dialogpt, blender, cleverbot, tencent, kuki, gpt3. For example, to query Blender Bot:

```
python experiment.py full blender 
```

- The visualization results and other measurements will be saved in `./figs/`

- For [Tencent](https://ai.qq.com/), [Kuki](https://dev.kuki.ai/dashboard), [Cleverbot](https://www.cleverbot.com/api/), and [GPT-3](https://openai.com/api/), access keys are required for API requests. Please click the link and create access keys following their instructions. After obtaining the access credentials, use the following command to export the credentials of the chatbot under test to the environment before running BiasAsker.

  ```bash
  export TENCENT_ID="your tencent id" # for Tencent
  export TENCENT_KEY="your tencent key" # for Tencent
  export KUKI_KEY="your kuki key" # for Kuki
  export CLEVERBOT_KEY="your cleverbot key" # for Cleverbot
  export GPT3_KEY="your gpt3 key" # for GPT-3
  ```

## Utilities

You can also run different utilities of BiasAsker separately.

**Generate queries and collect answers**

This utility can generate questions, query the chatbot, and collect the answers. It will save the result into `./save/<checkpt name>`. The result can be loaded by BiasAsker in the future to perform other tasks. If the experiment is interrupted, the saved result can also serve as a checkpoint to resume the experiment from where it stopped.

```
python experiment.py ask <bot name> <checkpt name> 
```

**Evaluate answers**

This utility will load question-answer data in `./save/<checkpt name>` and evaluate the answers according to the rules described in our paper and save the evaluation result in `./save/<checkpt name>_eval`. Same command can be used to resume evaluation from the checkpoint file.

```
python experiment.py eval <checkpt name> 
```

**Resume experiment**

To resume answer collection or answer evaluation from checkpoint file `./save/<checkpt name>`, use

```
python experiment.py resume <bot name> <checkpt name> # for answer collection
python experiment.py eval <checkpt name> # for answer evaluation
```

**Export data and visualization after evaluation**

To export all question-answer records or visualizations of the chatbot after evaluating answers, use the following code:

```
python experiment.py export <checkpt path> # for export records
python experiment.py plot <checkpt path> # for plot visualizations
```

all the figures (png files) and measurements (csv files) will be saved in `./figs/`

**Concurrent running**

BiasAsker will generate a large amount of questions to query the chatbot under test, one can speed up this process by first running several BiasAskers concurrently, each responsible for querying a subset of the questions, then merging the results of these BiasAskers. Detailed implementations are in **parallel.ipynb**.

## Test your own chatbot

Use BiasAsker to test your own chatbot in just two steps: 

- Create a class in `apis.py` that inherits from the *Bot* class, and overwrite the *respond* method where the input is a query (string) and the output is your chatbot's answer (string) to that query.
- Update the *bot_dict* in `experiment.py` to include your chatbot class.
