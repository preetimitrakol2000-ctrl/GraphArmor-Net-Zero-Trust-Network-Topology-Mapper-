#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "blast_radius.h"

// Creates a new adjacency list node
AdjListNode* new_adj_list_node(int dest, float weight) {
    AdjListNode* new_node = (AdjListNode*)malloc(sizeof(AdjListNode));
    if (new_node) {
        new_node->dest = dest;
        new_node->vulnerability_weight = weight;
        new_node->next = NULL;
    }
    return new_node;
}

// Creates a graph of V vertices
Graph* create_graph(int vertices) {
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    graph->num_vertices = vertices;
    graph->array = (AdjList*)malloc(vertices * sizeof(AdjList));

    for (int i = 0; i < vertices; i++) {
        graph->array[i].head = NULL;
    }
    return graph;
}

// Adds a directed edge to the network graph (representing data flow paths)
void add_edge(Graph* graph, int src, int dest, float weight) {
    AdjListNode* new_node = new_adj_list_node(dest, weight);
    new_node->next = graph->array[src].head;
    graph->array[src].head = new_node;
}

// Memory cleanup
void free_graph(Graph* graph) {
    if (!graph) return;
    for (int v = 0; v < graph->num_vertices; v++) {
        AdjListNode* crawl = graph->array[v].head;
        while (crawl) {
            AdjListNode* temp = crawl;
            crawl = crawl->next;
            free(temp);
        }
    }
    free(graph->array);
    free(graph);
}
