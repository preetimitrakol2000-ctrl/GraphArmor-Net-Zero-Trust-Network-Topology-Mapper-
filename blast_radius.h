#ifndef BLAST_RADIUS_H
#define BLAST_RADIUS_H

typedef struct AdjListNode {
    int dest;
    float vulnerability_weight; // Probability metric of exploit success (0.0 to 1.0)
    struct AdjListNode* next;
} AdjListNode;

typedef struct AdjList {
    AdjListNode* head;
} AdjList;

typedef struct Graph {
    int num_vertices;
    AdjList* array;
} Graph;

Graph* create_graph(int vertices);
void add_edge(Graph* graph, int src, int dest, float weight);
void free_graph(Graph* graph);

#endif // BLAST_RADIUS_H
