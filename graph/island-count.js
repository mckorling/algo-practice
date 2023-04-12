const grid = [
  [0, 1, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0],
  [0, 1, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0]
];

// 1s = land, 0s = water
// count how many islands there are

const islandCount = (grid) => {
  const visited = new Set();
  let count = 0;

  // loop through the grid
  // call helper function on each pos
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (exploreGrid(grid, i, j, visited)) {
        count++;
        // console.log(visited);
      }
    }
  }
  
  return count;
}

// return immediately if pos is out of bounds, or water, or already visited
const exploreGrid = (grid, r, c, visited) => {
  const rowInbounds = 0 <= r && r < grid.length;
  const colInbounds = 0 <= c && c < grid[0].length;
  if (!rowInbounds || !colInbounds) {
    return false;
  }

  if (grid[r][c] === 0) {
    return false;
  }

  const pos = r + ',' + c;
  if (visited.has(pos)) return false;

  visited.add(pos);
  exploreGrid(grid, r + 1, c, visited);
  exploreGrid(grid, r, c + 1, visited);
  exploreGrid(grid, r - 1, c, visited);
  exploreGrid(grid, r, c - 1, visited);

  return true; // means a brand new island was explored
}

console.log(islandCount(grid)); // 4