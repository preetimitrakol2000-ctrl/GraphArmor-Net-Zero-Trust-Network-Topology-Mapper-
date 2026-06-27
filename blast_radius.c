#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "blast_radius.h"

// Exported functions for cross-language execution mapping
#ifdef _WIN32
    __declspec(dllexport) Graph* init_network(int vertices);
    __declspec(dllexport) void link_devices(Graph* graph, int src, int dest, float weight);
    __declspec(dllexport) void calculate_blast_radius(Graph* graph, int start_vertex, int* blast_zone, int* zone_size);
    __declspec(dllexport) void destroy_network(Graph* graph);
#endif

Graph* init_network(int vertices) {
    return create_graph(vertices);
}

void link_devices(Graph* graph, int src, int dest, float weight) {
    add_edge(graph, src, dest, weight);
}

// BFS traversal algorithm to find all compromised nodes downstream
void calculate_blast_radius(Graph* graph, int start_vertex, int* blast_zone, int* zone_size) {
    bool* visited = (bool*)malloc(graph->num_vertices * sizeof(bool));
    for (int i = 0; i < graph->num_vertices; i++) {
        visited[i] = false;
    }

    // Standard BFS Queue allocation array
    int* queue = (int*)malloc(graph->num_vertices * sizeof(int));
    int front = 0, rear = 0;

    visited[start_vertex] = true;
    queue[rear++] = start_vertex;
    
    int count = 0;

    while (front < rear) {
        int current_vertex = queue[front++];
        blast_zone[count++] = current_vertex;

        AdjListNode* temp = graph->array[current_vertex].head;
        while (temp) {
            int adj_vertex = temp->dest;
            if (!visited[adj_vertex]) {
                visited[adj_vertex] = true;
                queue[rear++] = adj_vertex;
            }
            temp = temp->next;
        }
    }

    *zone_size = count;
    free(visited);
    free(queue);
}

void destroy_network(Graph* graph) {
    free_graph(graph);
}
