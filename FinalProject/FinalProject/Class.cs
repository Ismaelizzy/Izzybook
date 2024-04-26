using Microsoft.Extensions.Hosting;

namespace FinalProject
{

	public class User
	{
		public string UserId { get; set; }
		public string HashedPassword { get; set; }
		public string ProfilePicture { get; set; }
		public List<Post> Feed { get; set; }

		public void CreateUser() { }
		public bool Login() { return false; }
		public void Logout() { }
		public void EditProfile() { }
		public void AddFriend(User friend) { }
		public void RemoveFriend(User friend) { }
		public List<User> GetFriends() { return new List<User>(); }
		public List<Post> GetFeed() { return new List<Post>(); }
	}
}
