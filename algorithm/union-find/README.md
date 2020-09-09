- disjoint set
- union - find 알고리즘
<트리구조로 구현>
같은 집합 : 하나의 트리
집합 번호 = 루트노드

make-set(x)
각 노드는 모두 루트 노드이므로 N개의 루트 노드 생성 및 자기 자신으로 초기화한다.
union(x, y)
x, y의 루트 노드를 찾고 다르면 y를 x의 자손으로 넣어 두 트리를 합한다.
시간 복잡도: O(N)보다 작으므로 find 연산이 전체 수행 시간이 지배한다

find(x)
노드의 집합 번호는 루트 노드이므로, 루트 노드를 확인하여 같은 집합인지 확인한다.
시간 복잡도: 트리의 높이와 시간 복잡도가 동일하다. (최악: O(N-1))

int root[MAX_SIZE];
for (int i = 0; i < MAX_SIZE; i++)
    parent[i] = i;
parent의 인덱스는 각 원소들을 나타낸다.


<기본 알고리즘>
/* find(x): 재귀 이용 */

int find(int x) {
    // 루트 노드는 부모 노드 번호로 자기 자신을 가진다.
    if (root[x] == x) {
        return x;
    } else {
        // 각 노드의 부모 노드를 찾아 올라간다.
        return find(root[x]);
    }
}

/* union(x, y) */
void union(int x, int y){
    // 각 원소가 속한 트리의 루트 노드를 찾는다.
    x = find(x);
    y = find(y);

    root[y] = x;
}

최악의 경우 = 트리 구조가 완전 비대칭인 경우
연결 리스트 형태
트리의 높이가 최대가 된다.
원소의 개수가 N일 때, 트리의 높이가 N-1이므로 union과 find(x)의 시간 복잡도가 모두 O(N)이 된다.
배열로 구현하는 것보다 비효율적이다.

<path - compression>
find 연산 최적화
/* 초기화 */
int root[MAX_SIZE];
for (int i = 0; i < MAX_SIZE; i++) {
  root[i] = i;
}

/* find(x): 재귀 이용 */
int find(int x) {
  if (root[x] == x) {
      return x;
  } else {
      // "경로 압축(Path Compression)"
      // find 하면서 만난 모든 값의 부모 노드를 root로 만든다.
      return root[x] = find(root[x]);
  }
}

union 연산 최적화
/* 초기화 */
int root[MAX_SIZE];
int rank[MAX_SIZE]; // 트리의 높이를 저장할 배열
for (int i = 0; i < MAX_SIZE; i++) {
  root[i] = i;
  rank[i] = 0; // 트리의 높이 초기화
}

/* find(x): 재귀 이용 */
int find(int x) { // 동일
}

/* union1(x, y): union-by-rank 최적화 */
void union(int x, int y){
   x = find(x);
   y = find(y);

   // 두 값의 root가 같으면(이미 같은 트리) 합치지 않는다.
   if(x == y)
     return;

   // "union-by-rank 최적화"
   // 항상 높이가 더 낮은 트리를 높이가 높은 트리 밑에 넣는다. 즉, 높이가 더 높은 쪽을 root로 삼음
   // 그러면 트리의 높이가 늘어나지 않아 find연산하는 경우 최악의 시간복잡도를 피할 수 있음
   if(rank[x] < rank[y]) {
     root[x] = y; // x의 root를 y로 변경
   } else {
     root[y] = x; // y의 root를 x로 변경

     if(rank[x] == rank[y])
       rank[x]++; // 만약 높이가 같다면 합친 후 (x의 높이 + 1)
   }
}