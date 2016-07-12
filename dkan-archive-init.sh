
# DKAN branch or tag to use.
DKAN_VERSION="7.x-1.x"

# Try to grab archived dkan to speed up bootstrap.
URL="https://s3-us-west-2.amazonaws.com/nucivic-data-dkan-archives/dkan-$DKAN_VERSION.tar.gz"
wget -q -c "$URL"
mv dkan-$DKAN_VERSION.tar.gz ../
cd ..
tar -xzf dkan-$DKAN_VERSION.tar.gz
rm -rf dkan/docroot/sites/default/settings.php
cd dkan
bash dkan/dkan-init.sh dkan --skip-init --deps
ahoy drush "-y --verbose si minimal --sites-subdir=default --account-pass='admin' --db-url=$DATABASE_URL install_configure_form.update_status_module=\"'array\(FALSE,FALSE\)'\""
ahoy drush sql-drop -y && ahoy dkan sqlc < backups/last_install.sql && \
echo "Installed dkan from backup"