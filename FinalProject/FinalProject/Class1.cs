namespace FinalProject
{
	public class Post
	{
		public string PostId { get; set; }
		public string Content { get; set; }
		public string Image { get; set; } // Assuming image is stored as byte array
		public string UserId { get; set; }
		public User CreatedBy { get; set; }

		public void CreatePost() { }
		public void EditPost() { }
		public void DeletePost() { }
		public Post GetPostById(string postId) { return new Post(); }
		public List<Post> GetUserPosts(User user) { return new List<Post>(); }
	}
}
