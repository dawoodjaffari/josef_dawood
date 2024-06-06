<template>
  <div class="container-fluid" style="padding-top: 40px">
    <!-- Page Heading -->
    <div class="d-sm-flex align-items-center justify-content-between mb-4">
      <h1 class="h3 mb-0 text-gray-800"></h1>

      <a
        href="#"
        class="d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm"
        @click="createblog"
        ><i class="fas fa-download fa-sm text-white-50"></i> New Blog Post</a
      >
    </div>

    <!-- Content Row -->
    <div class="row">
      <!-- Earnings (Monthly) Card Example -->
      <div class="col-xl-3 col-md-6 mb-4" @click="toggleBlogDiv">
        <div class="card border-left-primary shadow h-100 py-2">
          <div class="card-body">
            <div class="row no-gutters align-items-center">
              <div class="col mr-2">
                <div
                  class="text-xs font-weight-bold text-primary text-uppercase mb-1"
                >
                  Total Blogs
                </div>
                <div class="h5 mb-0 font-weight-bold text-gray-800">
                  {{ blogList.length }}
                </div>
              </div>
              <div class="col-auto">
                <a
                  ><i
                    class="bi bi-plus-circle-fill"
                    style="color: black; font-size: 30px; text-align: right"
                     @click="createblog"  
                  ></i
                ></a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-xl-3 col-md-6 mb-4" @click="toggleUserDiv">
        <div class="card border-left-success shadow h-100 py-2">
          <div class="card-body">
            <div class="row no-gutters align-items-center">
              <div class="col mr-2">
                <div
                  class="text-xs font-weight-bold text-success text-uppercase mb-1"
                >
                  Total Users
                </div>

                <div class="h5 mb-0 font-weight-bold text-gray-800">
                  {{ userList.length }}
                </div>
              </div>
              <div class="col-auto">
                <i
                  class="bi bi-plus-circle-fill"
                  style="color: green; font-size: 30px; text-align: right"
                  @click="addNewUserModal"
                ></i>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-xl-3 col-md-6 mb-4" @click="toggleCategoryDiv">
        <div class="card border-left-success shadow h-100 py-2">
          <div class="card-body">
            <div class="row no-gutters align-items-center">
              <div class="col mr-2">
                <div
                  class="text-xs font-weight-bold text-danger text-uppercase mb-1"
                >
                  Total Category
                </div>
                <div class="h5 mb-0 font-weight-bold text-gray-800">
                  {{ categoryList.length }}
                </div>
              </div>
              <div class="col-auto">
                <i
                  class="bi bi-plus-circle-fill"
                  style="color: red; font-size: 30px; text-align: right"
                 @click="addNewCategoryModal"></i>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Pending Requests Card Example -->
      <div class="col-xl-3 col-md-6 mb-4">
        <div class="card border-left-warning shadow h-100 py-2">
          <div class="card-body">
            <div class="row no-gutters align-items-center">
              <div class="col mr-2">
                <div
                  class="text-xs font-weight-bold text-warning text-uppercase mb-1"
                >
                  Total Comments
                </div>
                <div class="h5 mb-0 font-weight-bold text-gray-800">18</div>
              </div>
             
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Content Row -->

    <div class="row" v-if="showBlogDiv">
      <!-- Area Chart -->
      <div class="col-xl-12 col-lg-12">
        <div class="card shadow mb-4">
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">Title</th>
                <th scope="col">Category</th>
                <th scope="col">Create Date</th>
                <th scope="col"></th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="main in blogList" :key="main.id">
                <td>{{ main.title }}</td>
                <td>{{ main.category }}</td>
                <td>{{ formatDate(main.date) }}</td>
                <td>
                  <i class="bi bi-pencil-square" style="color: orange" @click="editBlog(main)"></i>
                </td>
                <td><i class="bi bi-trash" style="color: red"   @click="deleteBlog(main.id)"></i></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="row" v-if="showUserDiv">
      <div class="col-xl-12 col-lg-12">
        <div class="card shadow mb-4">
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">Fist Name</th>
                <th scope="col">Last Name</th>
                <th scope="col">Email Address</th>
                <th scope="col"></th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="main in userList" :key="main.id">
                <td>{{ main.firstname }}</td>
                <td>{{ main.lastname }}</td>
                <td>{{ main.email }}</td>
                <td>
                  <i
                    class="bi bi-pencil-square"
                    style="color: orange"
                    :style="{ color: isAdmin ? 'orange' : 'gray', filter: isAdmin ? '' : 'blur(2px)', cursor: isAdmin ? 'pointer' : 'default' }"
                    @click="isAdmin && openUserModal(main)"
                  ></i>
                </td>
                <td><i class="bi bi-trash" style="color: red"  
                :style="{ color: isAdmin ? 'orange' : 'gray', filter: isAdmin ? '' : 'blur(2px)', cursor: isAdmin ? 'pointer' : 'default' }"
                @click="isAdmin && deleteUser(main.id)"></i></td>
              </tr>
            </tbody>
          </table>
          <div class="card-body">
            <div class="chart-area">
              <canvas id="myAreaChart"></canvas>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row" v-if="showCategoryDiv">
      <div class="col-xl-12 col-lg-12">
        <div class="card shadow mb-4">
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">Name</th>
                <th scope="col"></th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="main in categoryList" :key="main.id">
                <td>{{ main.name }}</td>
                <td>
                  <i class="bi bi-pencil-square" 
                  style="color: orange" @click="showModalCategory(main)" ></i>
                </td>
                <td><i class="bi bi-trash" style="color: red" @click="deleteCategory(main.categoryId)"></i></td>
              </tr>
            </tbody>
          </table>
          <div class="card-body">
            <div class="chart-area">
              <canvas id="myAreaChart"></canvas>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="modal" v-if="showModal">
    <div class="modal-content">
      <span class="close" @click="closeModal">&times;</span>
      <h2>{{ userStatus }}</h2>
      <form @submit.prevent="saveUserData">
        <div class="row">
          <label for="username">Username:</label>
          <input
            type="text"
            id="username"
            v-model="userFormData.username"
            :disabled="isDisabled"
            required
          />
        </div>

        <div class="row">
          <label for="password">Password:</label>
          <input
            type="password"
            id="password"
            v-model="userFormData.password"
            :disabled="isDisabled"
            required
          />
        </div>

        <div class="row">
          <label for="email">Email:</label>
          <input
            type="email"
            id="email"
            v-model="userFormData.email"
            :disabled="disableFields"
            required
          />
        </div>

        <div class="row">
          <label for="firstName">First Name:</label>
          <input
            type="text"
            id="firstName"
            v-model="userFormData.firstname"
            required
          />
        </div>

        <div class="row">
          <label for="lastName">Last Name:</label>
          <input
            type="text"
            id="lastName"
            v-model="userFormData.lastname"
            required
          />
        </div>
        <br />

        <div class="row">
          <button style="color: white; background-color: green" type="submit">
            Save
          </button>
        </div>
      </form>
    </div>
  </div>


   <div class="modal" v-if="showCategoryModal">
    <div class="modal-content">
      <span class="close" @click="closeCategoryModal">&times;</span>
      <h2>{{ categoryStatus }}</h2>
      <form @submit.prevent="saveCategoryData">
        <div class="row">
          <label for="name">Name</label>
          <input
            type="text"
            id="name"
            v-model="categoryFormData.name"
            required
          />
        </div>
        <br />

        <div class="row">
          <button style="color: white; background-color: green" type="submit">
            Save
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "DashboardPage",
  data() {
    return {
      showUserDiv: false,
      showBlogDiv: true,
      showCategoryDiv: false,
      showCommentDivL: false,
      totalComment: 0,
      categoryList: [],
      blogList: [],
      userList: [],
      showModal: false,
      userStatus: "Add New User",
      categoryStatus: "Add New Category",
      showCategoryModal: false,
      isDisabled: false,
      catid: '',
      id:'',
      username:'',
      userid:'',
      isAdmin: false,
      userFormData: {
        username: "",
        password: "",
        email: "",
        firstName: "",
        lastName: "",
      },
      categoryFormData: {
        name: "",
      }
    };
  },
  created() {
    this.userid = localStorage.getItem("id");
    this.username = localStorage.getItem("username");
    if(this.username == "admin"){
      this.isAdmin = true;
    }
    
    this.fetchCategories();
    this.fetchBlog();
    this.fetchUsers();

  },
  methods: {
    createblog() {
      const id = 0;
      this.$router.push({ name: 'manageblog', params: { id } });
    },
    toggleUserDiv() {
      if (this.showUserDiv == false) {
        this.showUserDiv = true;
        this.showBlogDiv = false;
        this.showCategoryDiv = false;
        this.showCommentDiv = false;
      }
    },
    toggleBlogDiv() {
      if (this.showBlogDiv == false) {
        this.showUserDiv = false;
        this.showBlogDiv = true;
        this.showCategoryDiv = false;
        this.showCommentDiv = false;
      }
    },
    toggleCategoryDiv() {
      if (this.showCategoryDiv == false) {
        this.showUserDiv = false;
        this.showBlogDiv = false;
        this.showCategoryDiv = true;
        this.showCommentDiv = false;
      }
    },
    toggleCommentDiv() {
      if (this.showCategoryDiv == false) {
        this.showUserDiv = false;
        this.showBlogDiv = false;
        this.showCategoryDiv = false;
        this.showCommentDiv = true;
      }
    },
    fetchCategories() {
      this.categoryList = [];
      fetch("http://127.0.0.1:5000/categories", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch categories");
          }
          return response.json();
        })
        .then((data) => {
          this.categoryList = data.map((category) => {
            return {
              categoryId: category[0],
              name: category[1],
            };
          });
        })
        .catch((error) => {
          console.error("Error fetching categories:", error);
        });
    },
    fetchBlog() {
      fetch("http://127.0.0.1:5000/blogs", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch blogs");
          }
          return response.json();
        })
        .then((data) => {
          this.blogList = data.map((main) => {
            return {
              id: main[0],
              title: main[1],
              data: main[3],
              date: main[4],
              category: main[7],
              firstname: main[8],
              lastname: main[9],
            };
          });
        })
        .catch((error) => {
          console.error("Error fetching blogs:", error);
        });
    },
    fetchUsers() {
      this.userList = [];
      fetch("http://127.0.0.1:5000/users", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch users");
          }
          return response.json();
        })
        .then((data) => {
          console.log(data);
          this.userList = data.map((main) => {
            return {
              id: main[0],
              email: main[1],
              username: main[2],
              password:main[3],
              firstname: main[4],
              lastname: main[5],
            };
          });
        })
        .catch((error) => {
          console.error("Error fetching users:", error);
        });
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      return new Intl.DateTimeFormat("default", { dateStyle: "long" }).format(
        date
      );
    },
    openUserModal(model) {
      this.showModal = true;
      this.userStatus = "Update User";
      this.isDisabled = true;
      this.userFormData.username = model.username;
      this.userFormData.password = model.password;
      this.userFormData.email = model.email;
      this.userFormData.firstname = model.firstname;
      this.userFormData.lastname = model.lastname;
      this.id = model.id;
    },
    addNewUserModal() {
      console.log("work");
      this.showModal = true;
      this.userStatus = "Add New User";
      this.isDisabled = false;
    },
    closeModal() {
      this.showModal = false;
      this.userFormData.username = "";
      this.userFormData.password = "";
      this.userFormData.email = "";
      this.userFormData.firstname = "";
      this.userFormData.lastname = "";
    },

    showModalCategory(model) {
      this.showCategoryModal = true;
      this.userStatus = "Update Category";
      this.categoryFormData.name = model.name;
      this.catid = model.categoryId;
    },
    addNewCategoryModal() {
      this.showCategoryModal = true;
      this.userStatus = "Add New Category";
    },
    closeCategoryModal() {
      this.showCategoryModal = false;
      this.categoryFormData.name = "";
    },
    saveUserData() {

      let method = 'PUT';
      
      if(this.userStatus == "Add New User"){
          method = 'POST';
      }
      fetch("http://127.0.0.1:5000/users", {
        method: method,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: this.id,
          username:this.userFormData.username,
          password:this.userFormData.password,
          email:this.userFormData.email, 
          firstname:this.userFormData.firstname, 
          lastname:this.userFormData.lastname,
          isActive: 1 
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          
          alert("Successfully Saved!");
          this.closeModal();
          this.fetchUsers();
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("Failed to make request. Please try again.");
        });
    },
    deleteUser(id){
      const isConfirmed = window.confirm("Are you sure you want to delete this user?");
      if (isConfirmed) {
       fetch("http://127.0.0.1:5000/users/"+id, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to delete users");
          }
           alert("Successfully Deleted!");
           this.fetchUsers();
        })
        .catch((error) => {
          console.error("Error deleting users:", error);
        });
      }
    },
    saveCategoryData(){

    let method = 'PUT';
      
      if(this.userStatus == "Add New Category"){
          method = 'POST';
      }
      fetch("http://127.0.0.1:5000/categories", {
        method: method,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: this.catid,
          name:this.categoryFormData.name
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          
          alert("Successfully Saved!");
          this.closeCategoryModal();
          this.fetchCategories();
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("Failed to make request. Please try again.");
        });


    },
     deleteCategory(id){
      const isConfirmed = window.confirm("Are you sure you want to delete this category?");
      if (isConfirmed) {
       fetch("http://127.0.0.1:5000/categories/"+id, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to delete category");
          }
           alert("Successfully Deleted!");
           this.fetchCategories();
        })
        .catch((error) => {
          console.error("Error deleting category:", error);
        });
      }
    },
    deleteBlog(id){
      const isConfirmed = window.confirm("Are you sure you want to delete this Blog?");
      if (isConfirmed) {
       fetch("http://127.0.0.1:5000/blogs/"+id, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to delete blog");
          }
           alert("Successfully Deleted!");
           this.fetchBlog();
        })
        .catch((error) => {
          console.error("Error deleting blog:", error);
        });
      }
    },
    editBlog(main){
      const id = main.id;
      this.$router.push({ name: 'manageblog', params: { id } });
    }
  },
};
</script>


<style scoped>
/* Styles for the modal */
.modal {
  display: block;
  position: fixed; /* Stay in place */
  z-index: 10; /* Sit on top */
  flex-direction: row;
  flex-wrap: nowrap;
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.4); /* Black w/ opacity */
}

/* Modal content */
.modal-content {
  background-color: #fefefe;
  margin: 15% auto; /* 15% from the top and centered */
  padding: 20px;
  border: 1px solid #888;
  width: 50%; /* Could be more or less, depending on screen size */
}

/* Close button */
.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>