import numpy as np
import individual
import problem
# convert from npy to txt file and shows blocks and their layers
# YOU MUST CHANGE THE TXT FILE STRING AND SPECIFY WHICH GEN TO WRITE IN OUTPUTS
# OTHERWISE IT WILL OVERWRITE!!!!!
#
# THIS IS NOT POLISHED CODE!!!!!!
def convert(individuals):
    s = ''
    for i, ind_1 in enumerate(individuals):
        print('\nIndividual number {}:'.format(i))
        ind_1 = individual.build_individual(problem.skeleton_genome, ind_1)
        print("fitness", ind_1.fitness.values)
        for i in range(1,ind_1.num_blocks+1):
            # get block dictionary containing metadata + block obj
            curr_block = ind_1.skeleton[i]

            # show block name
            print('\n{} Block:'.format(curr_block['nickname']))

            # go through each active genome node and print
            for active_node in curr_block['block_object'].active_nodes[:-1]:
                # print all layers except last node because it is just a number
                # i'm not sure why, but it isn't a layer type so it should probably be ignored
                print(curr_block['block_object'][active_node])
                s += str(curr_block['block_object'][active_node])
    return s

data = np.load('outputs_cifar/gen4_pop.npy', allow_pickle=True)
s = convert(data)
#text_file = open("gen6_pop.txt", "w")
#text_file.write(s)
