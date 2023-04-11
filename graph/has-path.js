// Acyclic solutions!!!

const hasPathStack = (graph, src, dst) => {
  const stack = [src];
  while (stack.length > 0) {
    const curr = stack.pop();
    if (curr === dst) return true;

    for (let neighbor of graph[curr]) {
      stack.push(neighbor);
    }
  }
  return false;
}

const hasPathRecursive = (graph, src, dst) => {
    if (src === dst) return true;


  for (let neighbor of graph[src]) {
    if (hasPathRecursive(graph, neighbor, dst) === true) {
      return true;
    }
  }
  return false;
}

const hasPathQueue = (graph, src, dst) => {
  const queue = [src];
  while (queue.length > 0) {
    const curr = queue.shift();
    if (curr === dst) return true;
    
    for (let neighbor of graph[curr]) {
      queue.push(neighbor);
    }
  }
  return false;
}

const graph = {
  f: ['g', 'i'],
  g: ['h'],
  h: [],
  i: ['g', 'k'],
  j: ['i'],
  k: []
}
console.log(hasPathStack(graph, 'f', 'k')); // true
console.log(hasPathStack(graph, 'f', 'j')); // false

console.log(hasPathRecursive(graph, 'f', 'k')); // true
console.log(hasPathRecursive(graph, 'f', 'j')); // false

console.log(hasPathQueue(graph, 'f', 'k')); // true
console.log(hasPathQueue(graph, 'f', 'j')); // false