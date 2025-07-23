import { useEffect, useState } from "react";
import { getGroups } from "../api/group";
import GroupCard from "../components/GroupCard";
import Navbar from "../components/Navbar";

export default function GroupPage() {
  const [groups, setGroups] = useState([]);

  useEffect(() => {
    async function fetchGroups() {
      const data = await getGroups();
      setGroups(data);
    }
    fetchGroups();
  }, []);

  return (
    <div>
      <Navbar />
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 p-6">
        {groups.map((group) => (
          <GroupCard key={group.id} group={group} />
        ))}
      </div>
    </div>
  );
}