import backend as svhs
import blender as blender


def main():
    print("\n \n Please enter the query\n")
    query = str(input())
    response1 = svhs.query_engine.query(query)
    # print("response 1")
    # print(response1)
    #query_results = svhs.query_engine.query(query)
    score = response1.source_nodes[0].score
    response2 = blender.llm_chain.run(query)
    # print("response 2")
    # print(response2)
    final =""

    if(score > 0.6):
        final = response1
    else:
        prompt = " I'm sorry! I am still a beta version & you are asking something out of my knowledge base (Zero to IPO by David Smith). Plaese stick to the domain knowledge. However, I can converse with my artfical inteligence."
        final = prompt+ "\n"+ response2
    print(final)


while(True):
    main()