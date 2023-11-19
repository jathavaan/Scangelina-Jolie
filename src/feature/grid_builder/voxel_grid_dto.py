import open3d as o3d


class VoxelGridDto:
    def __init__(
            self,
            voxel_grid: o3d.geometry.TriangleMesh,
            trees: o3d.geometry.TriangleMesh,
            buildings: o3d.geometry.TriangleMesh,
            terrain: o3d.geometry.TriangleMesh,
            river: o3d.geometry.TriangleMesh,
    ) -> None:
        self.voxel_grid = voxel_grid
        self.trees = trees
        self.buildings = buildings
        self.terrain = terrain
        self.river = river
