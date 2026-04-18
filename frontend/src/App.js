import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/students")
      .then(res => setStudents(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Student Manager</h1>

      <ul>
        {students.map(student => (
          <li key={student.id}>
            {student.name} - {student.course}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
