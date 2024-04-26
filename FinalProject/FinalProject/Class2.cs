namespace FinalProject
{
	public class Profile
	{
		public string FullName { get; set; }
		public string Bio { get; set; }
		public string Location { get; set; }
		public string Website { get; set; }

		public string GetFullName() { return FullName; }
		public string GetBio() { return Bio; }
		public string GetLocation() { return Location; }
		public string GetWebsite() { return Website; }
	}
}
