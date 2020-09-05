pushd /opt/mutable-config-usegalaxy-eu
cp /opt/galaxy/mutable-config/shed_tool_conf.xml .
git add .
git commit -m 'add new update'
git push
popd
