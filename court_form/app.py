<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Affidavit & Petition</title>
  <style>
    body {
      background-color: #3B0086;
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }

    .form-container {
      background-color: #3B0086;
      padding: 40px;
      border-radius: 12px;
      width: 400px;
      color: white;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
    }

    h2 {
      text-align: center;
      margin-bottom: 30px;
      color: #ffffff;
    }

    label {
      display: block;
      margin-top: 12px;
      font-weight: bold;
      font-size: 14px;
    }

    input[type="text"] {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
      border-radius: 6px;
      border: none;
      font-size: 14px;
      background-color: white;
      color: black;
    }

    button {
      margin-top: 25px;
      padding: 12px;
      width: 100%;
      background-color: white;
      color: #3B0086;
      border: none;
      font-weight: bold;
      border-radius: 6px;
      font-size: 16px;
      cursor: pointer;
    }

    button:hover {
      background-color: #e6dbff;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h2>Affidavit & Petition</h2>
    <form method="POST">
      <label>Petitioner Name:</label><input type="text" name="petitioner" required>
      <label>Respondent Name:</label><input type="text" name="respondent" required>
      <label>I.A. Number:</label><input type="text" name="ia_no" required>
      <label>OP/OS Number:</label><input type="text" name="op_no" required>
      <label>Petitioner Age:</label><input type="text" name="age" required>
      <label>Occupation:</label><input type="text" name="occupation" required>
      <label>Father's Name:</label><input type="text" name="father_name" required>
      <label>Address:</label><input type="text" name="address" required>
      <label>Filed On (DD-MM-YYYY):</label><input type="text" name="filed_on" required>
      <button type="submit">Generate Document</button>
    </form>
  </div>
</body>
</html>
