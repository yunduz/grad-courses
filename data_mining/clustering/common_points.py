import sys


def get_cluster_instances(f_path, num_clusters):
    clusters = []
    for i in range(num_clusters):
        clusters.append(set())

    with open(f_path, 'r') as f_in:
        #seek to the start of @data
        while True:
            line = f_in.readline()
            if line.startswith('@data'):
                break

        for line in f_in:
            line = line.split()
            if line:
                attrs = line[0].split(',')
                instance_id = int(attrs[0])
                cluster_id = int(attrs[-1].split('cluster')[1])
                clusters[cluster_id].add(instance_id)

    return sorted(clusters, key=lambda cluster: len(cluster), reverse=True)

def find_num_common_instances(clustering_a, clustering_b):
    for i in range(len(clustering_b)):
        for j in range(len(clustering_a)):
            #row_result.append(len(clustering_a.intersection(clustering_b)))
            sys.stdout.write(str(len(clustering_a[j].intersection(clustering_b[i]))))
            sys.stdout.write('\t')
        sys.stdout.write('\n')

cluster_6 = get_cluster_instances('/home/yunduz/CMPT741/Assn3/1_b/6clusters.arff', 6)
cluster_4 = get_cluster_instances('/home/yunduz/CMPT741/Assn3/1_b/4clusters.arff', 4)

cluster_6_2 = get_cluster_instances('/home/yunduz/CMPT741/Assn3/1_b/6clusters_2attrs.arff', 6)

# for i in range(len(cluster_6)):
#     print len(cluster_6[i])

find_num_common_instances(cluster_6, cluster_4)
print '-----------------'
find_num_common_instances(cluster_6, cluster_6_2)