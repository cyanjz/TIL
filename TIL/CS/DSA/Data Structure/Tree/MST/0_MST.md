# MST (Minimum Spanning Tree)
## 개요
정점의 수가 $|V|$이고 간선의 수가 |E|인 무방향 그래프를 생각해보자.

모든 정점을 포함하고 간선의 수가 |V|-1인 tree를 생각해 볼 수 있다.

$$
\text{there exists a Tree such that } |V_t| = |V| \text{ and } |E_t| = |V|-1
\\
\text{where } V_t = V \text{ and } E_t \subseteq E
$$

그러한 tree는 하나의 그래프에서 다양한 형태로 존재할 수 있다.

graph 내의 tree 중에서 간선의 가중치의 합이 최소인 tree를 MST라 한다.

$$
W_{MST} \leq W_{SpanningTree}
$$

## 알고리즘
대표적으로 kruskal과 prim 두 가지 알고리즘이 MST를 찾기 위해 사용된다.

두 알고리즘의 핵심 차이는 아래와 같이 요약할 수 있다.

Prim : MST를 점진적으로 확장시키면서 MST에 weight가 가장 낮은 edge의 정점을 추가해나가는 방식.

kruskal : 가장 가중치가 낮은 edge를 추가한다. 이때, cycle을 허용하지 않기 위해서 <a href='../../Disjoint_set&Union_find/Disjoint_set.md'>disjoint set</a>을 사용한다.

