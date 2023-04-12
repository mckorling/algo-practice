const grid = [
  [0, 1, 0, 0, 1, 0],
  [1, 1, 1, 1, 1, 0],
  [0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0],
  [1, 1, 0, 1, 1, 0],
  [1, 0, 0, 0, 0, 0]
];

const smallestIsland = (grid) => {
  const visited = new Set();
  let minimum = grid.length * grid[0].length;
  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      if (grid[r][c] === 1 && !visited.has(r + ',' + c)) {
        let size = countIslandSize(grid, r, c, visited);
        minimum = Math.min(minimum, size);
      }
    }
  }
  return minimum;
}

const countIslandSize = (grid, r, c, visited) => {
  const rowInbounds = 0 <= r && r < grid.length;
  const colInbounds = 0 <= c && c < grid[0].length;
  if (!rowInbounds || !colInbounds) return 0;
  if (grid[r][c] === 0) return 0;
  let pos = r + ',' + c;
  if (visited.has(pos)) return 0;

  visited.add(pos);
  let size = 1;
  size += countIslandSize(grid, r+1, c, visited);
  size += countIslandSize(grid, r-1, c, visited);
  size += countIslandSize(grid, r, c+1, visited);
  size += countIslandSize(grid, r, c - 1, visited);
  return size;
}

console.log(smallestIsland(grid));