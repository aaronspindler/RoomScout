echo "Deploying Roomscout.ca"

echo "Renaming Files"
mv Roomscout/settings.py Roomscout/settings_dev.py
mv Roomscout/settings_prod.py Roomscout/settings.py

cd ..
git add .
echo -n "Enter commit message: "
read commitmsg
git commit -m "$commitmsg"

git push

echo "Changing filenames back"
mv Roomscout/settings.py Roomscout/settings_prod.py
mv Roomscout/settings_dev.py Roomscout/settings.py