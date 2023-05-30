// Make sure to include Axios library in your HTML file or import it if using a module system

// Initialize Axios with the backend URL
const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:5000", // Replace with your backend URL
});

// Function to handle login
async function login() {
  try {
    // Get the Firebase ID token
    const idToken = await firebase.auth().currentUser.getIdToken();

    // Send the ID token to the backend
    const response = await axiosInstance.post("/login", { idToken });

    // Retrieve the JWT access token from the response
    const accessToken = response.data.access_token;

    // Save the JWT access token in local storage or wherever needed
    localStorage.setItem("accessToken", accessToken);

    // Redirect or perform any other actions after successful login
    // ...
  } catch (error) {
    console.log(error);
    // Handle any errors that occur during login
    // ...
  }
}
