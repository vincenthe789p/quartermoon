<?php 
       
if ($_SERVER['REQUEST_METHOD'] == 'POST') { 
                   
    function get_data() { 
        $name = $_POST['name']; 
        $file_name='StudentsData'. '.json'; 
   
        if(file_exists("$file_name")) {  
            $current_data=file_get_contents("$file_name"); 
            $array_data=json_decode($current_data, true); 
                               
            $extra=array( 
                'name' => $_POST['name'], 
                'phone' => $_POST['phone'], 
                'email' => $_POST['email'], 
                'shelter' => $_POST['shelter'], 
                'health' => $_POST['health'], 
                'fam' => $_POST['fam'], 
                'other' => $_POST['other'],
                'message' => $_POST['message'],
            ); 
            $array_data[]=$extra; 
            return json_encode($array_data); 
        } 
        else { 
            $datae=array(); 
            $datae[]=array( 
                'name' => $_POST['name'], 
                'phone' => $_POST['phone'], 
                'email' => $_POST['email'], 
                'shelter' => $_POST['shelter'], 
                'health' => $_POST['health'], 
                'fam' => $_POST['fam'], 
                'other' => $_POST['other'],
                'message' => $_POST['message'],
            ); 
            return json_encode($datae);    
        } 
    } 
  
    $file_name='StudentsData'. '.json'; 
      
    if(file_put_contents("$file_name", get_data())) { 
        echo '<p style="text-align:center;color:white;">Thank you for your request. We will be in touch with you as soon as possible.</p>'; 
    }                 
    else { 
        echo 'Error!';                 
    } 
} 
       
?> 