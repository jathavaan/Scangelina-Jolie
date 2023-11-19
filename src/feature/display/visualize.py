import open3d as o3d


class Visualize:
    @staticmethod
    def mesh(*voxel_mesh: o3d.geometry.TriangleMesh) -> None:
        title: str = f'Triangle mesh with {len(voxel_mesh)} voxel meshes'
        o3d.visualization.draw_geometries([*voxel_mesh], window_name=title)

