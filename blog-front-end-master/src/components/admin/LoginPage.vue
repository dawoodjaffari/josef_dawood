<template>
  <div class="container" style="padding-top: 50px;">
    <div>
      <div class="d-lg-flex half">
        <div class="bg order-1 order-md-2">
          <img src="../../assets/img/app/login_image.jpg" class="img-fluid" style="width: 650px">
        </div>
        <div class="contents order-2 order-md-1">
          <img src="" alt="">
          <div class="container">
            <div class="row align-items-center justify-content-center">
              <div class="col-md-7" v-if="signIn">
                <div class="mb-4">
                  <h3>Signin</h3>
                  <p class="mb-4">The BlogPage admin console. Please login with your admin credentials.</p>
                </div>
                <form @submit.prevent="logIn">
                  <div class="form-group first">
                    <label for="username">Username</label>
                    <input type="text" class="form-control" id="username" v-model="username">
                  </div>
                  <div class="form-group last mb-3">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" v-model="password">
                  </div>
                  <input type="submit" value="Log In" class="btn btn-block btn-primary">
                   <p v-if="passwordError" style="color: red;">{{ passwordError }}</p>
                </form>
              </div>

             <div class="col-md-7" v-if="!signIn">
                <div class="mb-4">
                  <h3>Signup</h3>
                  <p class="mb-4">Ready to become a part of our blogging community? Sign up now to unleash your creativity, share your thoughts with the world  </p>
                </div>
                <form @submit.prevent="register">
                  <div class="form-group first">
                    <label for="username">First Name</label>
                     <input type="text" class="form-control" v-model="firstName" required>
                  </div>
                  <div class="form-group first">
                    <label for="username">Last Name</label>
                     <input type="text" class="form-control" v-model="lastName"  required>
                  </div>
                  <div class="form-group first">
                    <label for="username">Email</label>
                     <input type="email" class="form-control" v-model="email" required>
                  </div>
                  <div class="form-group first">
                    <label for="username">Username</label>
                     <input type="text" class="form-control" v-model="username"  required>
                  </div>
                  <div class="form-group last mb-3">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" v-model="password" required>
                  </div>
                  <input type="submit" value="register" class="btn btn-block btn-primary">
                  <p v-if="passwordError" style="color: red;">{{ passwordError }}</p>
                </form>
              </div>
              <p v-if="!signIn">Don't have an account? <a style="color: green" @click="signup"> Signup</a></p>
              <p v-if="signIn">Already have an account? <a style="color: green" @click="signup"> Signin</a></p>
            </div>
            
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      firstName: '',
      lastName: '',
      email:'',
      username: '',
      password: '',
      passwordError:'',
      signIn : true,
      id: "",
    };
  },
  created(){
    this.id = localStorage.getItem("id");
    if(this.id !== null){
      this.$router.push('/dashboard');
    }
  },
  methods: {
    logIn() {

      fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          password:this.password,
          username:this.username 
        })
      })
        .then((response) => {

          if (response.status == 401) {
            this.passwordError = 'Invalid username or password';
          }else{
            return response.json();
          }
          
        })
        .then((data) => {
          console.log(data)
          localStorage.setItem("id",data[5]);
          localStorage.setItem("username",data[1]);
         // this.$router.push('/dashboard');
          this.username = '';
          this.password = '';
          window.location.reload();

        })
        .catch((error) => {
          console.error("Error fetching categories:", error);
        });
    },

    // fetch("http://127.0.0.1:5000/login", {
    //     method: 'POST',
    //     headers: {
    //       "Content-Type": "application/json",
    //     },
    //     body: JSON.stringify({
    //       password:this.password,
    //       username:this.username 
    //     }),
    //   })
    //     .then((response) => {
    //       console.log(response.json())
    //       if (response.status == 401) {
    //         this.passwordError = 'Invalid username or password';
    //       }
          
    //       return response.json()
          
    //     }) 
    //     .then((data) => {
    //       console.log(data)
    //       //  if(response.status == 200){
    //       //   this.$router.push('/dashboard');
    //       //   this.username = '';
    //       //   this.password = '';
    //       // }
    //     })
    //     .catch((error) => {
    //       console.error("Error:", error);
    //       alert("Failed to make request. Please try again.");
    //     });
   // },
     register() {
  
      if (!this.validatePassword(this.password)) {
        this.passwordError = "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.";
        return;
      }

      fetch("http://127.0.0.1:5000/register", {
        method: 'POST',
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email:this.email,
          password:this.password,
          firstName:this.firstName, 
          lastName:this.lastName, 
          username:this.username 
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }   
          alert("Registered successfully");
          this.username = '';
          this.password = '';
          this.email = '';
          this.firstName = '';
          this.lastName = '';
          this.signup();
        
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("Failed to make request. Please try again.");
        });
    },
    validatePassword(password) {
      const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$/;
      return passwordRegex.test(password);
    },
    signup(){
      if( this.signIn == true){
        this.signIn =false;
      }else{
        this.signIn = true;
      }
     
    }
  }
};
</script>
